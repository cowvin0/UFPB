set.seed(123)

ar_series <- arima.sim(list(order = c(1, 0, 0), ar = 0.7), n = 100)
modelo_ar <- arima(ar_series, order = c(1, 0, 0))
previsoes_ar <- predict(modelo_ar, n.ahead = 15)$pre
