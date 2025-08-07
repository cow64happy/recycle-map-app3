import folium

m = folium.Map(location=[36.5, 127.8], zoom_start=7)

city_data = {
    '서울': {'location': [37.5665, 126.9780], 'amount': 1500000, 'color': 'red'},
    '부산': {'location': [35.1796, 129.0756], 'amount': 930000, 'color': 'orange'},
    '대구': {'location': [35.8722, 128.6025], 'amount': 790000, 'color': 'green'},
    '대전': {'location': [36.3504, 127.3845], 'amount': 770000, 'color': 'green'},
    '광주': {'location': [35.1595, 126.8526], 'amount': 720000, 'color': 'green'}
}

for city, data in city_data.items():
    folium.Circle(
        location=data['location'],
        radius=data['amount'] * 0.01,
        color=data['color'],
        fill=True,
        fill_color=data['color'],
        fill_opacity=0.6,
        popup=f"{city} (2023): {data['amount']:,} kg"
    ).add_to(m)

m.save("recycle_map_2023.html")  # ✅ 이 부분이 핵심
