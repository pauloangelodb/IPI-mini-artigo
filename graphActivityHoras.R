install.packages("ggplot2")
library(ggplot2)

setwd("C:\\Users\\letic\\OneDrive\\Área de Trabalho\\PESQUISA\\mini artigo\\getHours")
df_activity <- read.table("commitHours.data", header = TRUE, sep=",")

df_activity

#pl <- ggplot(df_activity,aes(x = Hora, y=quantidade)) +
#scale_x_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
#scale_y_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
#geom_bar(stat = "identity", width=0.2)+

#theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Quantidade (commits)") +
#geom_line(color =" blue")

plot(df_activity, xaxt="none", main="Quantidade de commits em função da hora do dia")
axis(1, seq(0,25,1), font=2)
axis(2, seq(0,500,50), font=2)
geom_line(color =" blue")




#print(pl)
