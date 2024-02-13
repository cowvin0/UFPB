set.seed(123)

ar_series <- arima.sim(list(order = c(1, 0, 0), ar = 0.7), n = 100)
modelo_ar <- arima(ar_series, order = c(1, 0, 0))
previsoes_ar <- predict(modelo_ar, n.ahead = 15)$pre

Y=rep(0,30)
Y[3]=20
for(t in 4:30){
Y[t]=y[t-1]*0.8
}
Y
plot.ts(Y)
