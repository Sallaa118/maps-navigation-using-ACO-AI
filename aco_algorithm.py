import time
import osmnx as ox
import folium
from geopy.geocoders import Nominatim
import webbrowser
from datetime import datetime
import random
from collections import defaultdict

start_time = time.time()
# --- Konfigurasi OSMnx ---
ox.settings.log_console = True
ox.settings.use_cache = True
ox.settings.timeout = 300

# --- Fungsi untuk Menghitung Waktu Tempuh ---
def calculate_travel_times(distance):
    """Menghitung waktu tempuh untuk semua mode transportasi"""
    speeds = {
        'jalan_kaki': 1.4,  # ~5 km/jam
        'motor': 8.33,      # ~30 km/jam
        'mobil': 11.11      # ~40 km/jam
    }
    
    times = {}
    for mode, speed in speeds.items():
        seconds = distance / speed
        mins, secs = divmod(int(seconds), 60)
        times[mode] = f"{mins:02d}:{secs:02d}"
        
    return times

# --- Algoritma ACO ---
class AntColonyOptimized:
    def __init__(self, graph, ants=30, iterations=100):
        self.graph = graph
        self.ants = ants
        self.iterations = iterations
        # Inisialisasi feromon
        self.pheromones = defaultdict(lambda: defaultdict(float))
        for u, v, data in graph.edges(data=True):
            self.pheromones[u][v] = 1.0
            self.pheromones[v][u] = 1.0
        
    def find_path(self, start, end):
        best_path = None
        best_length = float('inf')
        
        for _ in range(self.iterations):
            for _ in range(self.ants):
                path, length = self._construct_path(start, end)
                if path and length < best_length:
                    best_path, best_length = path, length
                    # Update feromon untuk path terbaik
                    self._update_pheromones(best_path, best_length)
        
        return best_path, best_length
    
    def _construct_path(self, start, end):
        path = [start]
        current = start
        visited = set([start])
        total_length = 0
        
        while current != end:
            neighbors = [n for n in self.graph.neighbors(current) if n not in visited]
            if not neighbors:
                return None, float('inf')
            
            # Pilih next node berdasarkan feromon
            weights = [self.pheromones[current][n] for n in neighbors]
            total = sum(weights)
            if total == 0:
                return None, float('inf')
                
            probabilities = [w/total for w in weights]
            next_node = random.choices(neighbors, weights=probabilities, k=1)[0]
            
            path.append(next_node)
            visited.add(next_node)
            total_length += self.graph[current][next_node][0].get('length', 0)
            current = next_node
            
        return path, total_length
    
    def _update_pheromones(self, path, length):
        # Hanya update feromon untuk path terbaik
        delta = 1.0 / length if length > 0 else 0
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            self.pheromones[u][v] += delta
            self.pheromones[v][u] += delta

# --- Fungsi untuk Mendapatkan Waktu Sekarang ---
def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M %a, %d %b")

# --- Fungsi Pembungkus untuk Menemukan Rute ---
def find_shortest_path_aco(start, end):
    """Memanggil algoritma ACO untuk mencari rute"""
    try:
        # Load graph dari Universitas Bengkulu
        G = ox.graph_from_place("Universitas Bengkulu, Indonesia", network_type="walk")
        aco = AntColonyOptimized(G)
        path, distance = aco.find_path(start, end)
        return path, distance
    except Exception as e:
        print(f"Error ACO: {e}")
        return None, float('inf')

# --- Fungsi Utama ---
def main():
    # Load peta UNIB
    print("Memuat peta Universitas Bengkulu...")
    try:
        G = ox.graph_from_place("Universitas Bengkulu, Indonesia", network_type="walk")
        print("Peta berhasil dimuat!")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Input lokasi
    print("\n" + "="*40)
    print("UNIB PATHFINDER".center(40))
    print("="*40 + "\n")
    
    geolocator = Nominatim(user_agent="unib_navigator")
    
    start_place = input("Masukkan lokasi awal (contoh: Rektorat): ").strip()
    end_place = input("Masukkan lokasi tujuan (contoh: Fakultas Teknik): ").strip()

    # Geocoding
    def get_coords(place):
        try:
            location = geolocator.geocode(place + ", Bengkulu, Indonesia")
            if location:
                return (location.latitude, location.longitude)
        except Exception as e:
            print(f"Error geocoding {place}: {e}")
        return None

    start_coords = get_coords(start_place)
    end_coords = get_coords(end_place)
    
    if not start_coords or not end_coords:
        print("Lokasi tidak ditemukan!")
        return

    # Temukan node terdekat
    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

    # Hitung rute
    print("\nMenghitung rute terbaik...")
    path, distance = find_shortest_path_aco(start_node, end_node)
    
    if not path or distance == float('inf'):
        print("Tidak dapat menemukan rute!")
        return

    # Hitung waktu tempuh
    travel_times = calculate_travel_times(distance)
   
    # Buat peta
    print("Membuat peta interaktif...")
    center = ox.graph_to_gdfs(G, nodes=True, edges=False).unary_union.centroid
    m = folium.Map(location=[center.y, center.x], zoom_start=16)

    # Gambar rute
    if path:
        route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
        folium.PolyLine(
            route_coords, 
            color='#4285F4',
            weight=6,
            opacity=0.7,
            tooltip=f"Jarak: {distance:.0f} meter"
        ).add_to(m)

    # Tambahkan marker
    folium.Marker(
        location=[G.nodes[start_node]['y'], G.nodes[start_node]['x']],
        popup=f"<b>Start:</b> {start_place}",
        icon=folium.Icon(color='green', icon='flag')
    ).add_to(m)

    folium.Marker(
        location=[G.nodes[end_node]['y'], G.nodes[end_node]['x']],
        popup=f"<b>Tujuan:</b> {end_place}",
        icon=folium.Icon(color='red', icon='flag')
    ).add_to(m)

# Info box UNIB NAVIGATOR
    current_time = get_current_time()
    info_html = f"""
    <div style="position: fixed; bottom: 20px; left: 20px; 
                width: 300px; background: white; padding: 15px;
                border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                z-index: 9999; font-family: 'Segoe UI', Arial, sans-serif;
                border-top: 4px solid #4285F4;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 16px; font-weight: bold; color: #4285F4;">UNIB Navigator</div>
            <div style="font-size: 12px; color: #666;">{current_time}</div>
        </div>
        
        <div style="margin-bottom: 15px;">
            <div style="display: flex; margin-bottom: 5px;">
                <div style="width: 8px; height: 8px; background: #0F9D58; border-radius: 50%; margin-top: 5px; margin-right: 8px;"></div>
                <div style="font-size: 14px;"><b>Start:</b> {start_place[:20]}{'...' if len(start_place)>20 else ''}</div>
            </div>
            <div style="display: flex;">
                <div style="width: 8px; height: 8px; background: #DB4437; border-radius: 50%; margin-top: 5px; margin-right: 8px;"></div>
                <div style="font-size: 14px;"><b>Tujuan:</b> {end_place[:20]}{'...' if len(end_place)>20 else ''}</div>
            </div>
        </div>
        
        <div style="background: #F5F5F5; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span style="font-size: 14px;">Jarak</span>
                <span style="font-weight: bold; color: #4285F4;">{distance:.0f} meter</span>
            </div>
        </div>
        
        <div style="display: flex; justify-content: space-between; font-size: 13px;">
            <div style="text-align: center; padding: 5px; border-radius: 6px; background: #E8F0FE; color: #4285F4; width: 30%;">
                <div>🚶‍♂️</div>
                <div>{travel_times['jalan_kaki']}</div>
            </div>
            <div style="text-align: center; padding: 5px; border-radius: 6px; background: #E8F0FE; color: #4285F4; width: 30%;">
                <div>🏍</div>
                <div>{travel_times['motor']}</div>
            </div>
            <div style="text-align: center; padding: 5px; border-radius: 6px; background: #E8F0FE; color: #4285F4; width: 30%;">
                <div>🚗</div>
                <div>{travel_times['mobil']}</div>
            </div>
        </div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(info_html))

    # Simpan FIle HTML dan Buka Otomatis
    filename = "unib_navigation_aco.html"
    m.save(filename)
    print(f"\nPeta disimpan sebagai '{filename}'")
    webbrowser.open(filename)

if __name__ == "__main__":
    main()

end_time = time.time()

# Hitung durasi eksekusi
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.2f} detik")