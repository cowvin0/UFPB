library(tidyverse)
library(seastests)
library(tseries)

data <- vroom::vroom("salesdaily.xls") |>
  drop_na()

data |> pull(M01AE) |> adf.test()

data |> pull(M01AE) |> kpss.test()

data |> pull(M01AE) |> pp.test()

data |> pull(M01AE) |> ts(frequency = 12) |> kw()
