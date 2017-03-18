runTimes = textread('RunTimes.out');

%Calculate the slope of the line
slopeandIntercept = polyfit(log(runTimes(:,1)), log(runTimes(:,2)), 1); %Slope was 1.89

%Plot the runtime in log-log scale
loglog(runTimes(:,1),runTimes(:,2));
grid on;
title('Runtime of Weighted Edit Distance Dynamic Programming Algorithm');
xlabel('Length of String');
ylabel('Execution Time (s)');





