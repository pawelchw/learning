y = c(35, 34, 38, 35, 37)
est = mean(y)
se = sd(y)/sqrt(n)
int.50 = est + qt(c(.25,.75), n-1) * se
int.95 = est + qt(c(.025,.975), n-1) * se
print(int.95)