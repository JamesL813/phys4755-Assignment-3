#!/bin/R

library(ggplot2)
library(scales)

data1 <- read.csv("secant.csv", header=T, sep = ",")  # Read data

ggplot(data1) +                                       # Draw plot1
  geom_point(aes(delta, root), color = "darkred") +
  geom_hline(yintercept=1.162, linetype="dashed", color="grey") +
  theme_bw()
ggsave(file = "secant.pdf")                           # Export plot1

data2 <- read.csv("newton.csv", header=T, sep = ",")  # Read data

ggplot(data2) +                                       # Draw plot2
  geom_point(aes(rx, ry, color=delta)) +
  theme_bw()
ggsave(file = "newton.pdf")                           # Export plot2
