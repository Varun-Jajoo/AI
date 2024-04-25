father(dev,sagar).
father(dev,chirag).
father(bhavesh,dev).

father(diven,tanya).
father(diven,disha).

wife(devina,dev).
wife(rashi,chirag).
wife(neha,sagar).
wife(ritika,diven).
wife(tanya,bhavesh).
sister(tanya,disha).

male(dev).
male(bhavesh).
male(chirag).
male(diven).
male(sagar).

female(tanya).
female(disha).
female(devina).
female(ritika).
mother(X,Y):- wife(X,Z),father(Z,Y).
grandFather(X,Y):-father(X,Z),father(Z,Y).
grandMother(X,Y):- mother(X,Z),father(Z,Y).
