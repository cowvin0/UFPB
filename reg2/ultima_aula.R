library(gam)
library(betareg)

data("GasolineYield", package = "betareg")
gy3 <- betareg(yield ~ gravity + pressure + temp10 + temp, link="loglog",
data = GasolineYield)
summary(gy3)

gy <- betareg(yield ~ batch + temp, data = GasolineYield)
summary(gy)

plot(gy, which = 1, type = "pearson", sub.caption = "")

library(gamlss)
gamlss1<-gamlss(yield ~ gravity + pressure + temp10 + temp,
family=BE(mu.link = "logit", sigma.link = "logit"), data = GasolineYield)

# ----- Segundo Modelo -----

data("FoodExpenditure", package = "betareg")
fe_beta <- betareg(I(food / income) ~ income + persons, data = FoodExpenditure)
summary(fe_beta)