
bruteForce = textread('brutetimes.txt');
plot(bruteForce(:,1),bruteForce(:,2), 'blue'); hold on;

naive = textread('naivetimes.txt');
plot(naive(:,1),naive(:,2), 'green'); hold on;

enhanced = textread('enhancedtimes.txt')
plot(enhanced(:,1),enhanced(:,2), 'red'); hold on;

legend('bruteForce','naive','enhanced')
axis([0, 100000, 0 ,30])



