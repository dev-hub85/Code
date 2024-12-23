% Entry point for user interaction
diagnose_symptoms(Symptoms) :-
    (   % Diagnose measles
        member(fever, Symptoms),
        member(headache, Symptoms),
        member(rash, Symptoms),
        member(runny_nose, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: measles'), nl
    ;   % Diagnose covid19
        member(cough, Symptoms),
        member(shortness_of_breath, Symptoms),
        member(loss_of_taste_or_smell, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: covid19'), nl
    ;   % Diagnose common cold
        member(sneezing, Symptoms),
        member(sore_throat, Symptoms),
        member(chills, Symptoms),
        member(runny_nose, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: common cold'), nl
    ;   % Diagnose flu
        member(fever, Symptoms),
        member(body_ache, Symptoms),
        member(conjunctivitis, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: flu'), nl
    ;   % Diagnose mumps
        member(fever, Symptoms),
        member(sore_throat, Symptoms),
        member(swollen_glands, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: mumps'), nl
    ;   % Diagnose dengue
        member(headache, Symptoms),
        member(muscle_pain, Symptoms),
        member(joint_pain, Symptoms)
    ->  write('Based on the symptoms, the diagnosis is: dengue'), nl
    ;   % No match found
        write('No matching diagnosis found for the given symptoms.'), nl
    ).
