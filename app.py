from flask import Flask, render_template, request, jsonify
import networkx as nx

app = Flask(__name__)

# 建立地標與距離的圖結構
graph = nx.Graph()
edges = [
    ("臺北101", "中正紀念堂", 4),
    ("臺北101", "士林夜市", 2),
    ("中正紀念堂", "士林夜市", 1),
    ("中正紀念堂", "北投溫泉", 5),
    ("士林夜市", "北投溫泉", 8),
    ("士林夜市", "貓空纜車", 10),
    ("北投溫泉", "貓空纜車", 2),
    ("北投溫泉", "大安森林公園", 6),
    ("貓空纜車", "大安森林公園", 3),
]
graph.add_weighted_edges_from(edges)

# 地標評分
scores = {
    "臺北101": 9,
    "中正紀念堂": 8,
    "士林夜市": 7,
    "北投溫泉": 6,
    "貓空纜車": 5,
    "大安森林公園": 4,
}

# 動態決策過程的貪婪演算法
def select_spots_greedy_dynamic(start, scores, max_spots):
    selected_spots = [start]
    while len(selected_spots) < max_spots:
        current_spot = selected_spots[-1]
        candidates = {
            spot: scores[spot] / graph[current_spot][spot]['weight']
            for spot in graph.neighbors(current_spot)
            if spot not in selected_spots
        }
        if not candidates:
            break
        next_spot = max(candidates, key=candidates.get)
        selected_spots.append(next_spot)
    return selected_spots

# Dijkstra 演算法：計算選定地標之間的最短路徑
def find_shortest_path(graph, spots):
    shortest_path = []
    total_distance = 0
    for i in range(len(spots) - 1):
        path = nx.dijkstra_path(graph, spots[i], spots[i + 1], weight='weight')
        distance = nx.dijkstra_path_length(graph, spots[i], spots[i + 1], weight='weight')
        shortest_path.extend(path[:-1])
        total_distance += distance
    shortest_path.append(spots[-1])
    return shortest_path, total_distance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route', methods=['POST'])
def calculate_route():
    data = request.json
    start = "臺北101"  # 固定起始地標
    max_spots = int(data['max_spots'])

    # 改進的貪婪演算法選地標
    selected_spots = select_spots_greedy_dynamic(start, scores, max_spots)

    # Dijkstra 演算法計算路徑
    path, distance = find_shortest_path(graph, selected_spots)

    return jsonify({
        "selected_spots": selected_spots,
        "path": path,
        "distance": distance
    })

if __name__ == '__main__':
    app.run(debug=True)
