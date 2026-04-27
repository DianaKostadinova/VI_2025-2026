from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork, DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

if __name__ == '__main__':
    model = DiscreteBayesianNetwork([("WeakImmunity", "Infection"),
                           ("Infection", "Fever"),
                           ("Infection", "Cough"),
                           ("Infection", "Inflammation"),
                           ("Inflammation", "LabTest"),
                           ("WeakImmunity", "LabTest"),
                           ("Fever", "HospitalVisit"),
                           ("Cough", "HospitalVisit")])

    var_W = TabularCPD(variable='WeakImmunity', variable_card=2, values=[[0.8], [0.2]])
    var_I = TabularCPD(variable='Infection', variable_card=2, values=[[0.9, 0.3],
                                                                      [0.1, 0.7]],
                       evidence=['WeakImmunity'], evidence_card=[2])
    var_F = TabularCPD(variable="Fever", variable_card=2,
                       values=[[0.9, 0.2],
                               [0.1, 0.8]],
                       evidence=["Infection"], evidence_card=[2])

    var_C = TabularCPD(variable="Cough", variable_card=2,
                       values=[[0.8, 0.25],
                               [0.2, 0.75]],
                       evidence=["Infection"], evidence_card=[2])

    var_Inf = TabularCPD(variable="Inflammation", variable_card=2,
                         values=[[0.85, 0.15],
                                 [0.15, 0.85]],
                         evidence=["Infection"], evidence_card=[2])

    var_L = TabularCPD(variable="LabTest", variable_card=2,
                       values=[[0.90, 0.40, 0.15, 0.05],
                               [0.10, 0.60, 0.85, 0.95]],
                       evidence=["Inflammation", "WeakImmunity"], evidence_card=[2, 2])

    var_H = TabularCPD(variable="HospitalVisit", variable_card=2,
                       values=[[0.95, 0.30, 0.20, 0.05],
                               [0.05, 0.70, 0.80, 0.95]],
                       evidence=["Fever", "Cough"], evidence_card=[2, 2])

    model.add_cpds(var_W, var_I, var_F, var_C, var_Inf, var_L, var_H)
    infer = VariableElimination(model)

    q1 = infer.query(variables=['Infection'], evidence={'HospitalVisit': 1})
    print(f'P(Infection=1|HospitalVisit=1)={q1.values[1]}')


    q2 = infer.query(variables=['Infection'], evidence={'HospitalVisit': 1, 'LabTest': 1})
    print(f'P(Infection=1|HospitalVisit=1,LabTest=1)={q2.values[1]}')

    q3 = infer.query(variables=['WeakImmunity'], evidence={'LabTest': 1})
    print(f'P(WeakImmunity=1|LabTest=1)={q3.values[1]}')

    q4 = infer.query(variables=['Inflammation'], evidence={'LabTest': 1, 'WeakImmunity': 0})
    print(f'P(Inflammation=1|LabTest=1,WeakImmunity=0)={q4.values[1]}')

    q5 = infer.query(variables=['Fever'], evidence={'HospitalVisit': 1})
    print(f'P(Fever=1|HospitalVisit=1)={q5.values[1]}')

    q6 = infer.query(variables=['Cough'], evidence={'HospitalVisit': 1, 'Fever': 0})
    print(f'P(Cough=1|HospitalVisit=1,Fever=0)={q6.values[1]}')
