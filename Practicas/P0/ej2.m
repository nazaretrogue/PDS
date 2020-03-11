fSampling = 4000;
tSampling = 1/fSampling;
t = 0:tSampling:0.5;
fNote = [524 588 660 698 784 880 988];
Do = sin(2*pi*fNote(1)*t+2*pi*rand);
Re = sin(2*pi*fNote(2)*t+2*pi*rand);
Mi = sin(2*pi*fNote(3)*t+2*pi*rand);
Fa = sin(2*pi*fNote(4)*t+2*pi*rand);
Sol = sin(2*pi*fNote(5)*t+2*pi*rand);
La = sin(2*pi*fNote(6)*t+2*pi*rand);
Si = sin(2*pi*fNote(7)*t+2*pi*rand);
expWtCnst = 6;
expWt = exp(-abs(expWtCnst*t));
Do = Do.*expWt;
Re = Re.*expWt;
Mi = Mi.*expWt;
Fa = Fa.*expWt;
Sol = Sol.*expWt;
La = La.*expWt;
Si = Si.*expWt;
noteSequence = [Do Re Mi Fa Sol La Si];
soundsc(noteSequence, fSampling);

nFFT = 2^14;
tuneF = fft(noteSequence, nFFT);
magTune = abs(tuneF);
phaseTune = angle(tuneF);
phaseTune = unwrap(phaseTune);
fSpacing = fSampling/nFFT;
fAxis = fSampling/2:fSpacing:fSampling/2-fSpacing;
magTune = fftshift(phaseTune);
phaseTune = fftshift(phaseTune);

plot(fAxis,20*log10(magTune));
xlabel('Frequency F(Hz)');
ylabel('Magnitude X(F)');

figure(2);
plot(xAxis, phaseTune);
xlabel('Frequency F(Hz)');
ylabel('Phase X(F)');

figure(3);
spectrogram(noteSequence, 256, 0, [], fSampling);