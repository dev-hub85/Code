% Facts: A disease can be diagnosed based on symptoms.
diagnose(measles, Symptoms) :- member(fever, Symptoms), member(headache, Symptoms), member(rash, Symptoms), member(runny_nose, Symptoms).
diagnose(covid19, Symptoms) :- member(cough, Symptoms), member(shortness_of_breath, Symptoms), member(loss_of_taste_or_smell, Symptoms).
diagnose(common_cold, Symptoms) :- member(sneezing, Symptoms), member(sore_throat, Symptoms), member(chills, Symptoms), member(runny_nose, Symptoms).
diagnose(flu, Symptoms) :- member(fever, Symptoms), member(body_ache, Symptoms), member(conjunctivitis, Symptoms).
diagnose(mumps, Symptoms) :- member(fever, Symptoms), member(sore_throat, Symptoms), member(swollen_glands, Symptoms).
diagnose(dengue, Symptoms) :- member(headache, Symptoms), member(muscle_pain, Symptoms), member(joint_pain, Symptoms).

% Entry point for user interaction
diagnose_symptoms(Symptoms) :-
    diagnose(Diagnosis, Symptoms),
    write('Based on the symptoms, the diagnosis is: '), write(Diagnosis), nl.
