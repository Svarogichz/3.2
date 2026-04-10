import streamlit as st
import re
import time
from maze_solver import solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

def parse_maze(content):
    lines = content.strip().split('\n')
    maze_data = []
    for line in lines:
        row = [int(d) for d in re.findall(r'\d', line)]
        if row:
            maze_data.append(row)
    return maze_data

def find_points(maze):
    start, end = None, None
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == 2:
                start = (r, c)
            elif val == 3:
                end = (r, c)
    return start, end

def render_maze(maze, start, end, path=None):
    if path is None:
        path = []
    path_set = set(path)

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == start:
                display_row.append("🚀")
            elif (r_idx, c_idx) == end:
                display_row.append("🏁")
            elif (r_idx, c_idx) in path_set:
                display_row.append("🔹")
            elif col == 1:
                display_row.append("⬛")
            else:
                display_row.append("⬜")
        display_maze.append("".join(display_row))

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar
st.sidebar.header("OPCIONES DE LA APP")
st.sidebar.subheader("Carga el laberinto")
st.sidebar.caption("1=pared, 0=camino, 2=inicio, 3=final")

archivo = st.sidebar.file_uploader("", type=["txt"])
algorithm = st.sidebar.selectbox("Selecciona algoritmo", ["BFS", "DFS en proceso", "A* en proceso"])
solve_button = st.sidebar.button("Resolver Laberinto Cargado")

# Main
if archivo:
    content = archivo.read().decode("utf-8")
    maze = parse_maze(content)
    start, end = find_points(maze)

    if start is None or end is None:
        st.warning("El archivo debe contener un '2' (inicio) y un '3' (fin).")
    else:
        if not solve_button:
            render_maze(maze, start, end)

        if solve_button:
            if algorithm == "BFS":
                t0 = time.time()
                path, casillas = solve_maze_bfs(maze, start, end)
                elapsed = time.time() - t0

                if path:
                    st.success(f"BFS resuelto en {elapsed:.6f} s | Pasos: {casillas}")
                    render_maze(maze, start, end, path)
                else:
                    st.error("No se encontró una ruta válida.")
            else:
                st.info(f"{algorithm}: funcionalidad aún no implementada.")
                render_maze(maze, start, end)
else:
    st.info("Esperando archivo...")
