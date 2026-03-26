from constraint import *

if __name__ == "__main__":
    n_terms = int(input())
    papers = []
    papers_by_area = {}
    paper_area_map = {}
    for _ in range(10):
        line = input().strip().split()
        paper_id = line[0]
        area = line[1]
        papers.append(paper_id)
        paper_area_map[paper_id] = area
        if area not in papers_by_area:
            papers_by_area[area] = []
        papers_by_area[area].append(paper_id)

    problem = Problem(BacktrackingSolver())
    term_domain = list(range(1, n_terms + 1))

    for paper_id in papers:
        problem.addVariable(paper_id, term_domain)


    def max_4_in_term(*args):
        counts = {}
        for t in args:
            counts[t] = counts.get(t, 0) + 1
            if counts[t] > 4:
                return False
        return True


    problem.addConstraint(max_4_in_term, papers)

    for area, paper_list in papers_by_area.items():
        if len(paper_list) <= 4:
            problem.addConstraint(AllEqualConstraint(), paper_list)

    solution = problem.getSolution()

    for paper_id in papers:
        print(f"{paper_id} ({paper_area_map[paper_id]}): T{solution[paper_id]}")