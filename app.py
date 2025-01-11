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

# 地標評分（用於貪婪演算法）
scores = {
    "臺北101": 9,
    "中正紀念堂": 8,
    "士林夜市": 7,
    "北投溫泉": 6,
    "貓空纜車": 5,
    "大安森林公園": 4,
}

# 貪婪演算法：選擇最高評分的地標
def select_top_spots(scores, max_spots):
    return sorted(scores, key=scores.get, reverse=True)[:max_spots]

# Dijkstra 演算法：計算選定地標之間的最短路徑
def find_shortest_path(graph, spots):
    shortest_path = []
    total_distance = 0
    for i in range(len(spots) - 1):
        path = nx.dijkstra_path(graph, spots[i], spots[i + 1], weight='weight')
        distance = nx.dijkstra_path_length(graph, spots[i], spots[i + 1], weight='weight')
        shortest_path.extend(path[:-1])  # 避免重複添加節點
        total_distance += distance
    shortest_path.append(spots[-1])  # 加入最後一個地標
    return shortest_path, total_distance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route', methods=['POST'])
def calculate_route():
    data = request.json
    max_spots = int(data['max_spots'])

    # 貪婪演算法選地標
    selected_spots = select_top_spots(scores, max_spots)

    # Dijkstra 演算法計算路徑
    path, distance = find_shortest_path(graph, selected_spots)

    return jsonify({
        "selected_spots": selected_spots,
        "path": path,
        "distance": distance
    })

if __name__ == '__main__':
    app.run(debug=True)
