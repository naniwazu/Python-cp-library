from SCC import scc_graph


class two_sat:

    def __init__(self, N):
        self.N = N
        self.answer = []
        self.scc = scc_graph(2*N)

    def add_clause(self, i, f, j, g):
        assert 0 <= i < self.N
        assert 0 <= j < self.N
        self.scc.add_edge(2*i+(f == 0), 2*j+(g == 1))
        self.scc.add_edge(2*j+(g == 0), 2*i+(f == 1))

    def satisfiable(self):
        _, ids = self.scc.scc_ids()
        self.answer.clear()
        for i in range(self.N):
            if ids[2 * i] == ids[2 * i + 1]:
                self.answer.clear()
                return False
            self.answer.append(ids[2*i] < ids[2*i+1])
        return True
