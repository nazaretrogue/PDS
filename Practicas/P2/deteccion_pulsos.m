%Carga la señal
[s,Fs] = audioread('digitos.wav');

LWIN= 256;            % Longitud de la ventana.
SHIFT= 256;           % Desplazamiento. 
NFFT= 256;            % Número de frecuencias.

Nframes = floor((length(s)-LWIN)/SHIFT)+1;    % Número de ventanas
F = linspace(0,Fs/2,NFFT/2+1);                % Vector de frecuencias

for frame = 1:Nframes
    r = (frame-1)*SHIFT+[1:LWIN];
    
    Y = abs(fft(s(r)));      % Transformada de Fourier
    
    subplot(3,1,1);
    plot(s); hold on;
    stem(r,s(r),'r'); hold off;
    xlabel('Tiempo (s)');
    
    subplot(3,1,2);
    plot(F,Y(1:NFFT/2+1)); 
    xlabel('Frecuencia (Hz)'); 
    ylim([0 60])
    
    subplot(3,1,3);
    hold on;
    plot(F,Y(1:NFFT/2+1)); hold off;
    xlabel('Frecuencia (Hz)'); 
    
    drawnow;
    pause(0.1)
     
end
    
    
    
    
    


