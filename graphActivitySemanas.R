library(ggplot2)

setwd("C:\\Users\\letic\\OneDrive\\Área de Trabalho\\PESQUISA\\mini artigo")
df_activity <- read.table("activityWD.data", header = TRUE, sep=",")
Dias<-c("Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado","Domingo")

df_activity

pl <- ggplot(df_activity,aes(x = Dia, y=Frequencia)) +
  ggtitle("Commits em função do dia da semana")+
  
  theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Quantidade (commits)") +
  geom_line(lwd=1.5) +
  scale_x_continuous(breaks=(0:6),labels= Dias) +
  scale_y_continuous(limits = c(0, 1200))

print(pl)
