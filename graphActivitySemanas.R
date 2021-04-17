
library(ggplot2)

setwd("C:\\Users\\letic\\OneDrive\\Área de Trabalho\\PESQUISA\\mini artigo")
df_activity <- read.table("activityWD.data", header = TRUE, sep=",")

df_activity

#pl <- ggplot(df_activity,aes(x = Dia, y=Frequência)) +
#scale_x_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
#scale_y_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
#geom_bar(stat = "identity", width=0.2)+

#theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Quantidade (commits)") +
#geom_line(color =" blue")

plot(df_activity, xaxt="none", main="Quantidade de commits em função do dia da semana")
axis(1, seq(0,25,1), font=2)
axis(2, seq(0,1200,200), font=2)


#print(pl)
