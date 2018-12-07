# BBR-versus-Cubic-TCP-Experimentation-and-Analysis

The main goal of this project is to understand and compare the working of BBR and Cubic protocols under various circumstances by deploying servers at various locations, and to verify the fairness of  BBR.

Performed the following experiments to achieve our goal. The experiments include Real Environment using Amazon AWS and Simulated Environment using Traffic Control.

1)Conducted a measurement study by measuring the performance of BBR and Cubic protocols based on bandwidth across different servers and clients deployed in Canada, London, USA, India etc using Amazon’s cloud service, AWS.
2)Conducted a measurement study after simulating a constant packet loss using TC ( traffic control ) to compare the performance of BBR and cubic protocols based on bandwidth in lossy networks.
3)Conducted a measurement study by running Cubic and BBR protocols simultaneously on same server and client machines to check the fairness of BBR.
