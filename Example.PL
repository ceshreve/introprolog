pet(Pet):- member(Pet, [cat, dog, bunny, bird]).
toy(Toy):- member(Toy, [trampoline, pool, scooter, 'basketball hoop']).

all_different(A, B, C, D):-
    A \= B, A \= C, A \= D, B \= C, B \= D, C \= D.

all_pets_valid(P1, P2, P3, P4):-
    pet(P1), pet(P2), pet(P3), pet(P4),
    all_different(P1, P2, P3, P4).

all_toys_valid(T1, T2, T3, T4):-
    toy(T1), toy(T2), toy(T3), toy(T4),
    all_different(T1, T2, T3, T4).

solution(Houses):-
    Houses = [
       [red, RedPet, RedToy],
       [blue, BluePet, BlueToy],
       [yellow, YellowPet, YellowToy],
       [pink, PinkPet, PinkToy]
    ],
    all_pets_valid(RedPet, YellowPet, BluePet, PinkPet),
    all_toys_valid(RedToy, YellowToy, BlueToy, PinkToy),

    % Clue 1, the bunny doesn't live at the red or yellow house,
    % and it doesn't live with the pool or scooter %
    member(bunny, [BluePet, PinkPet]),
    \+ member([_, bunny, scooter], Houses),
    \+ member([_, bunny, pool], Houses),

    % Clue 2, the red house doesn't have the cat, but it has the
    % baseketball hoop
    member([red, _, 'basketball hoop'], Houses),
    \+ member([red, cat, _], Houses),
    % Alternate ways to write the above line:
    % member(cat, [BluePet, YellowPet, PinkPet]),
    % member(RedPet, [bird, bunny, dog])

    % Clue 3, the pink house has the bird
    member([pink, bird, _], Houses),

    % Clue 4, the cat lives with the pool
    member([_, cat, pool], Houses).
