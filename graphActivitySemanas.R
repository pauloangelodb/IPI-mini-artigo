library(ggplot2)

setwd("C:\\Users\\letic\\OneDrive\\Área de Trabalho\\PESQUISA\\mini artigo")
df_activity <- read.table("activityWD.data", header = TRUE, sep=",")
Dias<-c("Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado","Domingo")

df_activity

pl <- ggplot(df_activity,aes(x = Dia, y=Frequencia)) +
ggtitle("Commits por dia da semana")+

theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Quantidade (commits)") +
geom_line(color ="blue", lwd=1.5)+
scale_x_continuous(breaks=(0:6),labels= c("S", "T", "Q", "Q", "S", "S", "D"))


print(pl)

#plot(df_activity, xaxt="n",main="Quantidade de commits em função do dia da semana", type="l")
#axis(1, at=0:6, labels=Dias, font=2)
#axis(2, seq(0,1200,200), font=2)

