from pgmpy.models import BayesianNetwork, DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

if __name__ == '__main__':
    model = DiscreteBayesianNetwork([('B','S'),('S','D')])

    var_b = TabularCPD(variable='B', variable_card=2, values=[[0.7],[0.3]])
    var_s = TabularCPD(variable='S', variable_card=2, values=[[0.9,0.2],[0.1,0.8]],evidence=['B'],evidence_card=[2])
    var_d = TabularCPD(variable='D', variable_card=2, values=[[0.95,0.2],[0.05,0.8]],evidence=['S'],evidence_card=[2])

    model.add_cpds(var_b, var_s,var_d)
    infer = VariableElimination(model)

    q1 = infer.query(variables=['B'],evidence={'D':1})
    print(f'P(B=1|D=1)={q1.values[1]}')

    q2 = infer.query(variables=['B'], evidence={'S': 1})
    print(f'P(B=1|S=1)={q2.values[1]}')

    q3 = infer.query(variables=['B'], evidence={'S': 1, 'D': 1})
    print(f'P(B=1|S=1,D=1)={q3.values[1]}')