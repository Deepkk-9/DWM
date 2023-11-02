def calculate_pagerank(adjacency_matrix, damping_factor=0.85, max_iterations=100, epsilon=1e-8):
    num_nodes = len(adjacency_matrix)
    initial_pr = [1 / num_nodes] * num_nodes
    pr = initial_pr.copy()

    for _ in range(max_iterations):
        new_pr = [(1 - damping_factor) / num_nodes] * num_nodes

        for i in range(num_nodes):
            num_links = sum(adjacency_matrix[j][i] for j in range(num_nodes))
            if num_links == 0:
                num_links = num_nodes
            for j in range(num_nodes):
                if adjacency_matrix[j][i] == 1:
                    new_pr[j] += damping_factor * (pr[i] / num_links)

        if sum(abs(new_pr[i] - pr[i]) for i in range(num_nodes)) < epsilon:
            return new_pr

        pr = new_pr

    return pr


def get_page_ranks(adjacency_matrix, damping_factor=0.8, max_iterations=1, epsilon=1e-8):
    page_ranks = calculate_pagerank(
        adjacency_matrix, damping_factor, max_iterations, epsilon)
    return page_ranks


if __name__ == '__main__':

    adjacency_matrix = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
    ]

    node_page_ranks = get_page_ranks(adjacency_matrix)
    print("Page Ranks:")
    for i, page_rank in enumerate(node_page_ranks):
        print(f"Node {i+1}: {page_rank}")


# [[0, 1, 1, 0, 0, 0],
#  [1, 0, 0, 1, 1, 1],
#  [1, 0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0]]
