load muneca.asc;
plot(muneca);
Fs=8000;
N=length(muneca);
t=0:1/Fs:(N-1)/Fs;
plot(t,muneca)
%soundsc(muneca, Fs)
soundsc(yout, Fs);

