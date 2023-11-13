A fundamental assumption of stock market analysis is that stock behavior undergoes random fluctuations over time.

Brownian motion was named after Robert Brown for his discovery of the random motion exhibited by pollen particles immersed in water. These particles appeared to be struck by a large set of smaller particles traveling at random through the fluid (or medium). The collision with the pollen particles thus imparts a force in a certain direction, and this occurs many times per second, giving rise to the seemingly random and *continuous* motion of the pollen particles.

To "formalize" such a concept, a 1D random-walk implemented Brownian Motion would have its steps sampled from a normal distribution $N(0, dt)$. This is intuitively due to the fact that for a large change in time, a particle should have moved a larger distance.

Such a continuous random walk is called a **Wiener Process**, which is the mathematical embodiment of Brownian motion and actually samples from a normal distribution $N(0, \sqrt{dt})$. A system that has Brownian behavior can thus be studied over time using stochastic calculus, namely stock prices. The following stochastic differential equation:

$$
dS(t) = \mu S(t)dt + \sigma St d W(t)
$$

where the first term is called the drift term and the second term the diffusion term; can be shown to have the following solution [^1]:

$$
S(t) = S(0) \cdot e^{(\mu - \frac{1}{2} \sigma^2)t + \sigma W(t)}
$$

where $(W(t)$ is a Wiener process, $\mu$ is the mean stock price, $\sigma$ is its standard deviation, and $S(0)$ is the stock price at $t=0$. When Brownian motion is used in an exponential, the system itself is said to follow Geometric Brownian motion. In this case, we are then dealing with the changes in percentages of stock prices as opposed to stock price changes themselves.

In the plots below, the stock price of Nvidia Corporation was predicted by calculating the mean and standard deviation of the stock using data from 11 months ago to 5.5 months ago from Yahoo Finance. A prediction of the stock was then made for the current day using Monte Carlo statistical analysis, yielding the following results.

On the right, simulation of 10,000 random walks using the mean (average stock price) and standard deviation (volatility) extracted from NVIDIA data dating from December 2022 to mid-May 2023, shown on the left.

Prediction of stock price compared to the current stock price value, raw value, and natural log value.
