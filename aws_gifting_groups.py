''' 
Problem Statement: Group Connectivity Counting

Description:
Given a matrix representing relationships between nodes/members,
count the number of distinct groups where members are connected.

Key Characteristics:
- Input is a square matrix of strings '0' and '1'
- A '1' indicates a direct or indirect connection between two nodes
- Connections are symmetric and transitive
- Goal is to count the total number of unique, fully connected groups

Detailed Problem Explanation:
- Nodes are considered in the same group if they are connected directly or indirectly
- Connectivity can be through multiple intermediate nodes
- Self-connections are always present (a node is connected to itself)
- The matrix is square, with dimensions n x n
- Matrix is symmetric (if related[i][j] is '1', related[j][i] is also '1')

Parameters:
- related (list of str): A square matrix represented as a list of strings
    - Each string represents a row in the connectivity matrix
    - Each character is either '0' (no connection) or '1' (connected)

Returns:
- int: Number of distinct, fully connected groups in the network

Time Complexity: O(n²)
Space Complexity: O(n)

Example:
Input: 
related = [
    "1100",   # Node 0 connected to 0, 1
    "1100",   # Node 1 connected to 0, 1
    "0011",   # Node 2 connected to 2, 3
    "0011"    # Node 3 connected to 2, 3
]
Output: 2  # Two distinct groups: (0,1) and (2,3)

Visualization of the groups:
Group 1: Nodes 0 and 1 are connected
Group 2: Nodes 2 and 3 are connected
Total groups: 2

Constraints:
- 1 <= len(related) <= 300
- related[i][j] is either '0' or '1'
- related is a square matrix
- Connections are symmetric and reflexive'
'''


def dfs(node, related, visited):
    visited[node] = True
    for i in range(len(related)):
        # Si hay una relación (1) entre node e i, y i no ha sido visitado
        if i != node and related[node][i] == '1' and not visited[i]:
            dfs(i, related, visited)


def countGroups2(related):
    n = len(related)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            # Comenzar un nuevo grupo
            count += 1
            dfs(i, related, visited)

    return count


def get_relations(i, j, group, members, visited):
    # print(f"members[{i}][{j}]")
    if i > related_count - 1 or j > related_count - 1:
        # print("no mas parejas")
        visited[i] = True
        return
    if j not in group:
        if i == j:
            # print(f"self: {j}")
            group.add(i)
        elif int(members[i][j]) == 1:
            # print(f"members[{i}][{j}] -> relacion")
            if j not in visited:
                # print(f"añadir: {j}")
                group.add(j)
                # print (f"buscar en pareja {j}:")
                get_relations(j, 0, group, members, visited)

    get_relations(i, j + 1, group, members, visited)


def find_group(e, groups):
    for g in groups:
        if e in g:
            return g
    return set()


def countGroups(related):
    groups = []
    visited = [False] * len(related)
    for i in range(0, related_count):
        group = find_group(i, groups)
        get_relations(i, 0, group, related, visited)
        # print(f"group : {group}")
        if group not in groups:
            groups.append(group)
    # print(related)
    # print(groups)
    return len(groups)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)
    # print(related[:10])

    result = countGroups(related)

    fptr.write(str(result) + '\n')

    fptr.close()