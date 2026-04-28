from pgmpy.models import BayesianNetwork, DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

model =DiscreteBayesianNetwork([
    ('B', 'I'),
    ('M', 'I'),
    ('I', 'R'),
    ('I', 'T'),
    ('R', 'C'),
    ('T', 'C'),
    ('D', 'C')
])

cpd_B = TabularCPD('B', 2, [[0.65], [0.35]])  # P(B=1)=0.35
cpd_M = TabularCPD('M', 2, [[0.55], [0.45]])  # P(M=1)=0.45
cpd_D = TabularCPD('D', 2, [[0.75], [0.25]])  # P(D=1)=0.25

cpd_I = TabularCPD(
    'I', 2,
    [
        [1-0.12, 1-0.65, 1-0.72, 1-0.93],  # I=0
        [0.12,    0.65,    0.72,    0.93]   # I=1
    ],
    evidence=['B', 'M'],
    evidence_card=[2, 2]
)

cpd_R = TabularCPD(
    'R', 2,
    [
        [1-0.20, 1-0.80],
        [0.20,   0.80]
    ],
    evidence=['I'],
    evidence_card=[2]
)

cpd_T = TabularCPD(
    'T', 2,
    [
        [1-0.30, 1-0.85],
        [0.30,   0.85]
    ],
    evidence=['I'],
    evidence_card=[2]
)

cpd_C = TabularCPD(
    'C', 2,
    [
        [1-0.04, 1-0.32, 1-0.48, 1-0.75, 1-0.55, 1-0.78, 1-0.88, 1-0.97],
        [0.04,   0.32,   0.48,   0.75,   0.55,   0.78,   0.88,   0.97]
    ],
    evidence=['R', 'T', 'D'],
    evidence_card=[2, 2, 2]
)

model.add_cpds(cpd_B, cpd_M, cpd_D, cpd_I, cpd_R, cpd_T, cpd_C)

infer = VariableElimination(model)

print("P(I=1 | B=1, M=1):", infer.query(['I'], evidence={'B':1,'M':1}).values[1])
print("P(R=1 | I=1):", infer.query(['R'], evidence={'I':1}).values[1])
print("P(C=1 | T=1):", infer.query(['C'], evidence={'T':1}).values[1])
print("P(B=1 | I=1):", infer.query(['B'], evidence={'I':1}).values[1])
print("P(M=1 | I=1):", infer.query(['M'], evidence={'I':1}).values[1])
print("P(T=1 | C=1, R=0):", infer.query(['T'], evidence={'C':1,'R':0}).values[1])