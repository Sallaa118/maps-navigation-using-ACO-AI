import time as t
import osmnx as ox
import folium
from geopy.geocoders import Nominatim
import webbrowser
from datetime import time, datetime
import random
from collections import defaultdict

# Catat waktu mulai eksekusi
start_time = t.time()

# --- Konfigurasi OSMnx ---
ox.settings.log_console = True
ox.settings.use_cache = True
ox.settings.timeout = 300

# --- Database Lokal Gedung di Universitas Bengkulu ---
UNIB_BUILDINGS = {
    # Format: 'nama_gedung': (latitude, longitude)
    'gedung rektorat': (-3.7590495172423495, 102.27231460986346),
    'masjid baitul hikmah': (-3.758945132312725, 102.27600666694858),
    'perpustakaan': (-3.756806076798016, 102.27485462111163),
    'gerbang masuk kanan unib belakang': (-3.759561, 102.275189),
    'gerbang masuk kiri unib belakang' : (-3.759584, 102.275097),
    'gerbang masuk unib depan': (-3.759965, 102.267147),
    'gb 1': (-3.7568032921655625, 102.27372095056845),
    'gb 2': (-3.7578575751002457, 102.274037554275),
    'gb 3 & 4': (-3.7560850630710587, 102.27664495427499),
    'gb 5': (-3.7553463918453187, 102.27650213893024),
    'lptik': (-3.7585034389347047, 102.27501541748192),
    'gsg': (-3.757536160753844, 102.27655797563433),
    'dekanat teknik': (-3.7584642603667104, 102.27670099113969),
    'lab teknik': (-3.758891053967651, 102.27690975882886),
    'lab terpadu teknik': (-3.7585892834199925, 102.27735016612473),
    'stadion unib': (-3.7576442412116946, 102.27817155070424),
    'gedung fkip': (-3.756364599659421, 102.27746551161644),
    'fakultas kedokteran': (-3.7551337561874982, 102.27803206102215),
    'sekretariat ukm': (-3.756636058655066, 102.2757012915378),
    'dekanat fmipa': (-3.756028855847586, 102.2747136045303),
    'sekretariat bem fmipa': (-3.75578529907203, 102.27496036775979),
    'gedung fisika': (-3.7562055013818023, 102.27372386940291),
    'ruang baca pertanian': (-3.7571162998364276, 102.27283662942735),
    'lab agronomi': (-3.7570165757307543, 102.27271362771398),
    'glt': (-3.75809920273443, 102.27191958168342),
    'masjid darul ulum': (-3.757278224804399, 102.2675868394383),
    'lab ilmu tanah': (-3.7592326497010897, 102.27012662561205),
    'dekanat pertanian': (-3.759336210212976, 102.26921964529129),
    'dekanat hukum': (-3.760583199392584, 102.26844172291675),
    'lab hukum': (-3.7602660084096446, 102.26867339480454),
    'dekanat feb': (-3.7617198090691164, 102.26862389169713),
    'magister ilmu ekonomi': (-3.7624574876125974, 102.2686381084575),
    'jurusan ekonomi pembangunan': (-3.7617576387695197, 102.26894613829127),
    'upt bing': (-3.7607740664372096, 102.27036307553568),
    'gedung j': (-3.76030119474263, 102.2697707104651),
    'gedung k': (-3.761142906184093, 102.26990813916206),
    'gedung c': (-3.7590706965117002, 102.26791776641025),
    'danau unib': (-3.758445851629117, 102.27306446726114),
    'mushola shelter': (-3.7576982064708235, 102.27361705847183),
    'dekanat fisip': (-3.7590310709254973, 102.27417328919393),
    'dekanat fkip': (-3.75753414150989, 102.27504444750583),
    'gerbang keluar unib depan': (-3.759135, 102.267002),
    'gerbang keluar unib belakang': (-3.759366, 102.276245),
    'asrama pgsd': (-3.7617418863983096, 102.27160069043919),
    's2 matematika': (-3.7580570001381477, 102.27543890078353),
    'klinik pratama unib': (-3.7614596037430554, 102.2717675810424),
    'sekretariat teknik': (-3.7581980275566127, 102.27733334828312),
    'gerbang rektorat': (-3.765758, 102.268076),
    'lapangan olahraga unib': (-3.759384, 102.267357)
}

# --- Gate Controller System ---
class GateController:
    def __init__(self):
        # Jam operasional standar
        self.weekday_hours = (time(7, 0), time(18, 0))  # Senin-Jumat 07:00-18:00
        self.always_open_hours = (time(0, 0), time(23, 59, 59))  # 24 jam
        
    def is_weekday(self, weekday):
        return 0 <= weekday <= 4  # Senin-Jumat
        
    def is_between(self, check_time, time_range):
        start, end = time_range
        return start <= check_time <= end
    
    def check_side_gates_access(self, current_time):
        """Aturan khusus untuk gerbang belakang kiri/kanan"""
        current_time = current_time.time()
        if time(7, 0) <= current_time <= time(18, 0):
            return {
                'left_gate': {'entry': True,'directions': ['rektorat', 'straight', 'right_turn'], 'exit': False},
                'right_gate': {'entry': True,'directions': ['gsg'], 'straight': False, 'exit': False}
            }
        else:
            return {
                'left_gate': {'entry': True, 'directions': ['rektorat', 'straight', 'right_turn'], 'exit': False},
                'right_gate': {'entry': False, 'exit': True}
            }

    def check_front_gate(self, current_time):
        """Gerbang depan - Senin-Jumat 07:00-18:00"""
        if self.is_weekday(current_time.weekday()):
            return self.is_between(current_time.time(), self.weekday_hours)
        return False
        
    def check_rektorat_gate(self, current_time):
        """Gerbang rektorat - Senin-Jumat 07:00-18:00"""
        return self.check_front_gate(current_time)  # Aturan sama dengan gerbang depan

def get_gate_access():
    controller = GateController()
    current_time = datetime.now()
    side_gates = controller.check_side_gates_access(current_time)
    
    return {
        'access': {
            # Gerbang Depan
            'gate_in_front': controller.check_front_gate(current_time),
            'gate_out_front': controller.check_front_gate(current_time),
            
            # Gerbang Belakang (menggunakan aturan khusus)
            'gate_in_back_left': side_gates['left_gate']['entry'],
            'gate_out_back_left': side_gates['left_gate']['exit'],
            'gate_in_back_right': side_gates['right_gate']['entry'],
            'gate_out_back_right': side_gates['right_gate']['exit'],
            
            # Gerbang Rektorat
            'gate_rektorat': controller.check_rektorat_gate(current_time)
        },
        'directions': {
            'back_left': side_gates['left_gate'].get('directions', []),
            'back_right': side_gates['right_gate'].get('directions', [])
        }
    }

# --- Fungsi untuk Menghitung Waktu Tempuh Berdasarkan Jarak ---
def calculate_travel_times(distance):
    """
    Menghitung estimasi waktu tempuh berdasarkan jarak
    untuk beberapa moda transportasi: jalan kaki, motor, dan mobil.
    """
    speeds = {
        'jalan_kaki': 1.4,   # ~5 km/jam
        'motor': 8.33,       # ~30 km/jam
        'mobil': 11.11       # ~40 km/jam
    }
    
    times = {}
    for mode, speed in speeds.items():
        seconds = distance / speed
        mins, secs = divmod(int(seconds), 60)
        times[mode] = f"{mins:02d}:{secs:02d}"
        
    return times

# --- Kelas Algoritma Semut (Ant Colony Optimization) untuk Pencarian Jalur ---
class AntColonyOptimized:
    """
    Implementasi sederhana dari algoritma Ant Colony Optimization
    untuk menemukan jalur terpendek antara dua titik pada graf.
    """
    def __init__(self, graph, ants=30, iterations=100):
        self.graph = graph
        self.ants = ants
        self.iterations = iterations
        self.pheromones = defaultdict(lambda: defaultdict(float))
        self.gate_access = get_gate_access()['access']
        
        # Identifikasi node gerbang
        # In the AntColonyOptimized class __init__ method:
        self.gate_nodes = {
            'gerbang masuk kanan unib belakang': UNIB_BUILDINGS['gerbang masuk kanan unib belakang'],
            'gerbang masuk kiri unib belakang': UNIB_BUILDINGS['gerbang masuk kiri unib belakang'],
            'gerbang masuk unib depan': UNIB_BUILDINGS['gerbang masuk unib depan'],
            'gerbang keluar unib depan': UNIB_BUILDINGS['gerbang keluar unib depan'],
            'gerbang keluar unib belakang': UNIB_BUILDINGS['gerbang keluar unib belakang'],
            'gerbang rektorat': UNIB_BUILDINGS['gerbang rektorat']
        }
        
        # Inisialisasi feromon awal untuk semua edge yang diizinkan
        for u, v, data in graph.edges(data=True):
            if self._is_edge_allowed(u, v):
                self.pheromones[u][v] = 1.0
                self.pheromones[v][u] = 1.0
        
    def _is_edge_allowed(self, u, v):
        """Cek apakah edge melewati gerbang yang tidak diizinkan"""
        # Gerbang masuk depan
        if (u == self.gate_nodes['gerbang masuk unib depan'] or 
            v == self.gate_nodes['gerbang masuk unib depan']):
            return self.gate_access['gate_in_front']
        
        # Gerbang keluar depan
        if (u == self.gate_nodes['gerbang keluar unib depan'] or 
            v == self.gate_nodes['gerbang keluar unib depan']):
            return self.gate_access['gate_out_front']
        
        # Gerbang masuk kiri belakang
        if (u == self.gate_nodes['gerbang masuk kiri unib belakang'] or 
            v == self.gate_nodes['gerbang masuk kiri unib belakang']):
            # Selalu izinkan arah masuk (True), keluar tergantung gate_out_back_left
            if u == self.gate_nodes['gerbang masuk kiri unib belakang']:
                return True  # Selalu boleh masuk
            else:
                return self.gate_access['gate_out_back_left']  # Keluar sesuai aturan
        
        # Gerbang masuk kanan belakang
        if (u == self.gate_nodes['gerbang masuk kanan unib belakang'] or 
            v == self.gate_nodes['gerbang masuk kanan unib belakang']):
            # Masuk sesuai aturan, keluar selalu False (karena ada gerbang keluar terpisah)
            if u == self.gate_nodes['gerbang masuk kanan unib belakang']:
                return self.gate_access['gate_in_back_right']
            else:
                return False
        
        # Gerbang keluar belakang
        if (u == self.gate_nodes['gerbang keluar unib belakang'] or 
            v == self.gate_nodes['gerbang keluar unib belakang']):
            return self.gate_access['gate_out_back_right']
        
        # Gerbang rektorat
        if (u == self.gate_nodes['gerbang rektorat'] or 
            v == self.gate_nodes['gerbang rektorat']):
            return self.gate_access['gate_rektorat']
            
        return True
    
    def find_path(self, start, end):
        """
        Menjalankan iterasi semut untuk mencari jalur terpendek.
        """
        best_path = None
        best_length = float('inf')
        
        for _ in range(self.iterations):
            for _ in range(self.ants):
                path, length = self._construct_path(start, end)
                if path and length < best_length:
                    best_path, best_length = path, length
                    self._update_pheromones(best_path, best_length)
        
        return best_path, best_length
    
    def _construct_path(self, start, end):
        """
        Membangun jalur dari start ke end berdasarkan probabilitas.
        """
        path = [start]
        current = start
        visited = set([start])
        total_length = 0
        
        while current != end:
            neighbors = [n for n in self.graph.neighbors(current) if n not in visited]
            if not neighbors:
                return None, float('inf')
            
            # Filter neighbors berdasarkan gerbang yang diizinkan
            allowed_neighbors = []
            weights = []
            for n in neighbors:
                if self._is_edge_allowed(current, n):
                    allowed_neighbors.append(n)
                    weights.append(self.pheromones[current][n])
            
            if not allowed_neighbors:
                return None, float('inf')
                
            total = sum(weights)
            if total == 0:
                return None, float('inf')
                
            probabilities = [w / total for w in weights]
            next_node = random.choices(allowed_neighbors, weights=probabilities, k=1)[0]
            
            path.append(next_node)
            visited.add(next_node)
            total_length += self.graph[current][next_node][0].get('length', 0)
            current = next_node
            
        return path, total_length
    
    def _update_pheromones(self, path, length):
        """
        Memperbarui nilai feromon pada jalur terbaik yang ditemukan.
        """
        delta = 1.0 / length if length > 0 else 0
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            self.pheromones[u][v] += delta
            self.pheromones[v][u] += delta

# --- Fungsi untuk Mendapatkan Waktu Sekarang ---
def get_current_time():
    """
    Mengembalikan waktu sekarang dalam format yang ramah pengguna.
    """
    now = datetime.now()
    return now.strftime("%H:%M %a, %d %b")

# --- Fungsi untuk Mendapatkan Koordinat Gedung ---
def get_building_coords(place_name):
    """
    Mencari koordinat gedung berdasarkan nama.
    Pertama cek database lokal, jika tidak ada gunakan geocoding.
    """
    # Normalisasi nama tempat untuk pencarian case-insensitive
    normalized_name = place_name.lower().strip()
    
    # Cari di database lokal
    for name, coords in UNIB_BUILDINGS.items():
        if name in normalized_name or normalized_name in name:
            return coords
    
    # Jika tidak ditemukan di database lokal, gunakan geocoding
    try:
        geolocator = Nominatim(user_agent="unib_navigator")
        location = geolocator.geocode(place_name + ", Bengkulu, Indonesia")
        if location:
            return (location.latitude, location.longitude)
    except Exception as e:
        print(f"Error geocoding {place_name}: {e}")
    
    return None

# --- Fungsi Utama Program ---
def main():
    print("Memuat peta Universitas Bengkulu...")
    try:
        G = ox.graph_from_place("Universitas Bengkulu, Indonesia", network_type="drive_service")
        print("Peta berhasil dimuat!")
    except Exception as e:
        print(f"Error: {e}")
        return

    print("\n" + "=" * 40)
    print("UNIB NAVIGATOR".center(40))
    print("=" * 40 + "\n")
    
    start_place = input("Tentukan lokasi awal (contoh: Gedung Rektorat): ").strip()
    end_place = input("Tentukan lokasi tujuan (contoh: Fakultas Teknik): ").strip()

    # Dapatkan koordinat dari database lokal atau geocoding
    start_coords = get_building_coords(start_place)
    end_coords = get_building_coords(end_place)
    
    if not start_coords:
        print(f"Lokasi awal '{start_place}' tidak ditemukan!")
        return
    if not end_coords:
        print(f"Lokasi tujuan '{end_place}' tidak ditemukan!")
        return

    # Temukan node terdekat pada graf dari titik koordinat
    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

    # Verifikasi node yang dipilih
    start_node_coords = (G.nodes[start_node]['y'], G.nodes[start_node]['x'])
    end_node_coords = (G.nodes[end_node]['y'], G.nodes[end_node]['x'])
    
    # Hitung jarak antara titik yang diminta dan node yang dipilih
    def haversine(coord1, coord2):
        from math import radians, sin, cos, sqrt, atan2
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        
        R = 6371000  # radius bumi dalam meter
        phi1 = radians(lat1)
        phi2 = radians(lat2)
        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)
        
        a = sin(delta_phi/2)**2 + cos(phi1)*cos(phi2)*sin(delta_lambda/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        
        return R * c
    
    start_distance = haversine(start_coords, start_node_coords)
    end_distance = haversine(end_coords, end_node_coords)
    
    if start_distance > 100:  # Jika node terdekat > 100m dari lokasi sebenarnya
        print(f"Peringatan: Node awal ({start_distance:.0f}m dari lokasi sebenarnya)")
    if end_distance > 100:    # Jika node terdekat > 100m dari lokasi sebenarnya
        print(f"Peringatan: Node tujuan ({end_distance:.0f}m dari lokasi sebenarnya)")

    # Hitung rute menggunakan ACO
    print("\nMenghitung rute terbaik...")
    aco = AntColonyOptimized(G)
    path, distance = aco.find_path(start_node, end_node)
    
    if not path or distance == float('inf'):
        print("Tidak dapat menemukan rute! Mungkin ada gerbang yang sedang ditutup.")
        return

    # Hitung estimasi waktu tempuh
    travel_times = calculate_travel_times(distance)

    # Buat peta menggunakan folium
    print("Membuat peta interaktif...")
    center = ox.graph_to_gdfs(G, nodes=True, edges=False).unary_union.centroid
    m = folium.Map(location=[center.y, center.x], zoom_start=16)

    # Gambar jalur terbaik pada peta
    if path:
        route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
        folium.PolyLine(
            route_coords, 
            color='#4285F4',
            weight=6,
            opacity=0.7,
            tooltip=f"Jarak: {distance:.0f} meter"
        ).add_to(m)

    # Tambahkan marker titik awal dan tujuan
    folium.Marker(
        location=[start_coords[0], start_coords[1]],
        popup=f"<b>Titik Awal:</b> {start_place}",
        icon=folium.Icon(color='green', icon='flag')
    ).add_to(m)

    folium.Marker(
        location=[end_coords[0], end_coords[1]],
        popup=f"<b>Titik Tujuan:</b> {end_place}",
        icon=folium.Icon(color='red', icon='flag')
    ).add_to(m)

    # Tambahkan marker untuk node yang sebenarnya dipilih
    folium.CircleMarker(
        location=[G.nodes[start_node]['y'], G.nodes[start_node]['x']],
        radius=3,
        color='#00FF00',
        fill=True,
        fill_color='#00FF00',
        popup=f"Node Start: {start_node}"
    ).add_to(m)
    
    folium.CircleMarker(
        location=[G.nodes[end_node]['y'], G.nodes[end_node]['x']],
        radius=3,
        color='#FF0000',
        fill=True,
        fill_color='#FF0000',
        popup=f"Node End: {end_node}"
    ).add_to(m)

    # Tambahkan garis penghubung antara lokasi sebenarnya dengan node yang dipilih
    folium.PolyLine(
        locations=[start_coords, start_node_coords],
        color='#00FF00',
        weight=2,
        dash_array='5,5',
        tooltip=f"Jarak ke node: {start_distance:.0f} meter"
    ).add_to(m)
    
    folium.PolyLine(
        locations=[end_coords, end_node_coords],
        color='#FF0000',
        weight=2,
        dash_array='5,5',
        tooltip=f"Jarak ke node: {end_distance:.0f} meter"
    ).add_to(m)

    # Tambahkan marker untuk gerbang
    for gate_name, coords in UNIB_BUILDINGS.items():
        if 'gerbang' in gate_name.lower():  # Hanya ambil data gerbang
            folium.CircleMarker(
            location=[coords[0], coords[1]],  # Langsung pakai koordinat lokal
            radius=6,
            color='purple',
            popup=f"{gate_name.title()}",
            tooltip="Gerbang UNIB"
        ).add_to(m)

    # Info box tampilan bawah kiri
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
                <div style="font-size: 14px;"><b>Titik Awal:</b> {start_place[:20]}{'...' if len(start_place)>20 else ''}</div>
            </div>
            <div style="display: flex;">
                <div style="width: 8px; height: 8px; background: #DB4437; border-radius: 50%; margin-top: 5px; margin-right: 8px;"></div>
                <div style="font-size: 14px;"><b>Titik Tujuan:</b> {end_place[:20]}{'...' if len(end_place)>20 else ''}</div>
            </div>
        </div>
        
        <div style="background: #F5F5F5; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span style="font-size: 14px;">Jarak</span>
                <span style="font-weight: bold; color: #4285F4;">{distance:.0f} meter</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: #666;">
                <span>Node start: {start_distance:.0f}m dari lokasi</span>
                <span>Node end: {end_distance:.0f}m dari lokasi</span>
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

    # Info status gerbang
    gate_status_html = """
    <div style="position: fixed; top: 20px; right: 20px; 
                width: 280px; background: white; padding: 15px;
                border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                z-index: 9999; font-family: 'Segoe UI', Arial, sans-serif;
                border-top: 4px solid #4285F4;">
        <div style="font-size: 16px; font-weight: bold; color: #4285F4; margin-bottom: 10px;">
            Status Gerbang
        </div>
        <div style="font-size: 13px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span>Gerbang Masuk UNIB Depan:</span>
                <span style="color: {color_in_front};">{status_in_front}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span>Gerbang Keluar UNIB Depan:</span>
                <span style="color: {color_out_front};">{status_out_front}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span>Gerbang Kiri UNIB Belakang:</span>
                <span style="color: {color_in_back_left};">{status_in_back_left}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span>Gerbang Kanan UNIB Belakang:</span>
                <span style="color: {color_in_back_right};">{status_in_back_right}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span>Gerbang Rektorat:</span>
                <span style="color: {color_rektorat};">{status_rektorat}</span>
            </div>
        </div>
    </div>
    """.format(
        color_in_front="#0F9D58" if aco.gate_access['gate_in_front'] else "#DB4437",
        status_in_front="BUKA" if aco.gate_access['gate_in_front'] else "TUTUP",
        color_out_front="#0F9D58" if aco.gate_access['gate_out_front'] else "#DB4437",
        status_out_front="BUKA" if aco.gate_access['gate_out_front'] else "TUTUP",
        color_in_back_left="#0F9D58" if aco.gate_access['gate_in_back_left'] else "#DB4437",
        status_in_back_left="BUKA" if aco.gate_access['gate_in_back_left'] else "TUTUP",
        color_in_back_right="#0F9D58" if aco.gate_access['gate_in_back_right'] else "#DB4437",
        status_in_back_right="BUKA" if aco.gate_access['gate_in_back_right'] else "TUTUP",
        color_rektorat="#0F9D58" if aco.gate_access['gate_rektorat'] else "#DB4437",
        status_rektorat="BUKA" if aco.gate_access['gate_rektorat'] else "TUTUP"
    )
    
    m.get_root().html.add_child(folium.Element(gate_status_html))

    # Simpan file dan buka otomatis
    filename = "unib_navigation_aco.html"
    m.save(filename)
    print(f"\nPeta disimpan sebagai '{filename}'")
    webbrowser.open(filename)

# Jalankan program
if __name__ == "__main__":
    main()

# --- Hitung dan tampilkan waktu eksekusi ---
end_time = t.time()
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.2f} detik")
