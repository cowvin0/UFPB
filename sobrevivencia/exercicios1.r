library(tidyverse)
library(survival)
library(ggplot2)
library(ggfortify)
library(ranger)

# Questão 2

tempos <- c(
	0.19, 0.78, 0.96, 1.31,
	2.78, 3.16, 4.67, 4.85,
	6.5, 7.35, 8.27, 12.07,
	32.52, 33.91, 36.71, rep(37, 10)
)

cens <- c(
	rep(1, 15), rep(0, 10)
)

ekm <- survfit(Surv(tempos, cens) ~ 1)

# a)

tempo_mediano <- ((32.52 - 12.07) * 0.02) / 0.04 + 12.07

autoplot(ekm)

# b)

# c)

# Questão 3

tempos3 <- c(
	7, 34, 42, 63, 64, 74, 83, 84, 91,
	108, 112, 129, 133, 133, 139, 140, 140,
	146, 149, 154, 157, 160, 160, 165,
	173, 176, 185, 218, 225, 241, 248,
	273, 277, 279, 297, 319, 405, 417,
	420, 440, 523, 523, 583, 594, 1101,
	1116, 1146, 1226, 1349, 1412, 1417
)

cens3 <- c(
	rep(1, 5), 0, rep(1, 20),
	0, rep(1, 6), 0, 1, 0, rep(1, 5),
	0, rep(1, 3), 0, 1, 0, 0, 0, 1
)

ekm2 <- survfit(Surv(tempos3, cens3) ~ 1)

# Questão 4

tempos4 <- c(
	28, 89, 175, 195, 309, 377, 393, 421,
	447, 462, 709, 744, 770, 1106, 1206,
	34, 88, 137, 199, 280, 291, 299, 300,
	309, 351, 358, 369, 369, 370, 375, 382,
	392, 429, 451, 1119
)

cens4 <- c(
	rep(1, 5), rep(0, 4),
	1, rep(0, 5), rep(1, 6),
	0, 0, rep(1, 9), 0, 1, 0
)

grupos <- c(
	rep(1, 15), rep(2, 20)
)

ekm4 <- survfit(Surv(tempos4, cens4) ~ grupos)
survdiff(Surv(tempos4, cens4) ~ grupos, rho=0)

# Exercício 6

tempos6 <- c(
	31, 40, 43, 44, 46, 46, 47, 48,
	48, 49, 50, 50, rep(60, 8),
	48, 48, rep(49, 4), rep(50, 4),
	53, 53, rep(54, 3), rep(55, 5)
)

cens6 <- c(
	rep(1, 16), rep(0, 4),
	rep(1, 16), rep(0, 4)
)

grupos6 <- c(
	rep("A", 20),
	rep("B", 20)
)

ekm6 <- survfit(Surv(tempos6, cens6) ~ grupos6)

# a)

# Não existe diferença entre as embalagens

survdiff(Surv(tempos6, cens6) ~ grupos6)

# Exércicios 3.7

# Exercicio 1

surv_weibull <- \(t, alpha, gamma) {
	exp(-(t/alpha)^gamma)
}

# a) probabilidade do rato sobreviver sem tumos aos primeiros 30 dias
# ou 45 dias

dias_30 <- surv_weibull(30, 100, 2)
dias_45 <- surv_weibull(45, 100, 2)

# b) tempo médio

media <- 100 * gamma(3/2)

# c) tempo mediano

mediano <- 100 * sqrt(-log(0.5))

# d) taxa de falha

funcao_risco_weibull <- \(t, alpha, gamma) {
	gamma * t / (alpha ^ gamma)
}

taxafalha_30 <- funcao_risco_weibull(30, 100, 2)
taxafalha_45 <- funcao_risco_weibull(45, 100, 2)
taxafalha_60 <- funcao_risco_weibull(60, 100, 2)

# Questão 2



# Questão 3

tempos_cap3 <- c(
	0.19, 0.78, 0.96, 1.31, 2.78,
	3.16, 4.67, 4.85, 6.50, 7.35,
	8.27, 12.07, 32.52, 33.91, 36.71, rep(37, 10)
)

cens_cap3 <- c(
	rep(1, 15), rep(0, 10)
)

ajust1_exp <- survreg(
	Surv(tempos_cap3, cens_cap3) ~ 1, dist = "exponential"
)
lambda <- exp(ajust1_exp$coefficients[1])

ajust1_weibull <- survreg(
	Surv(tempos_cap3, cens_cap3) ~ 1, dist = "weibull"
)
alpha <- exp(ajust1_weibull$coefficients[1])
gama <- 1 / ajust1_weibull$scale

ajust1_lognormal <- survreg(
	Surv(tempos_cap3, cens_cap3) ~ 1, dist = "lognormal"
)

ekm_cap3_quest3 <- survfit(Surv(tempos_cap3, cens_cap3) ~ 1)
time <- ekm_cap3_quest3$time
ste <- exp(-time/lambda)
stw <- exp(-(time/alpha)^gama)
stln <- pnorm((-log(time) + ajust1_lognormal$coefficients)/ajust1_lognormal$scale)

tabela_ajustados <- tibble(
	Tempos = time,
	`Kaplan-Meier` = ekm_cap3_quest3$surv,
	Exponencial = ste,
	Weibull = stw,
	`Log-normal` = stln
)

tabela_ajustados |>
	ggplot(aes(x = `Kaplan-Meier`, y = Exponencial)) +
	geom_point() +
	geom_abline()

tabela_ajustados |>
	ggplot(aes(x = `Kaplan-Meier`, y = Weibull)) +
	geom_point() +
	geom_abline()

# a melhor foi a log-normal.

tabela_ajustados |>
	ggplot(aes(x = `Kaplan-Meier`, y = `Log-normal`)) +
	geom_point() +
	geom_abline()
