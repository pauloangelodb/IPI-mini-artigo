library(ggplot2)

setwd("C:\\Users\\letic\\OneDrive\\Área de Trabalho\\PESQUISA\\mini artigo\\getHours")
df_activity <- read.table("commitHours.data", header = TRUE, sep=",")

df_activity

pl <- ggplot(df_activity,aes(x = Hora, y=Frequencia)) +
  ggtitle("Commits em função da hora do dia")+
  
  theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Quantidade (commits)") +
  geom_line(lwd=1.5)+
  scale_y_continuous(limits = c(0, 500)) +
  scale_x_continuous(breaks=(0:23))

print(pl)
