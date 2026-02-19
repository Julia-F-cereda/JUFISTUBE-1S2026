USE jufisTube;
INSERT INTO `jufistube`.`genero`
(`nome_genero`,
`icone`,
`cor`)

VALUES
("Rock", "", "red"),
("Trap", "", "blue"),
("MPB", "", "#FACADA"),
("Hip Hop", "", "green"),
("New emo", "", "pink"),
("POP", "", "purple");

INSERT INTO `jufistube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)

VALUES
("2zdiniz",
"03:30",
"faixa amarela",
"https://cdn-images.dzcdn.net/images/cover/c77e5c5fd4586f3ef42b6492fbf7de76/0x1900-000000-80-0-0.jpg",
"Trap"),

("Charlie brown jr",
"03:40",
"é quente",
"https://i.scdn.co/image/ab67616d0000b2735e7cb9ed84348b98973c823f",
"Rock"),

("Lana del rey",
"3:20",
"the other woman",
"https://i.scdn.co/image/ab67616d00001e0259ae8cf65d498afdd5585634",
"POP"),

("Foi assim",
"4:40",
"Sotam",
"https://i1.sndcdn.com/artworks-ki4wGTuuzqSo-0-t500x500.jpg",
"Hip Hop"),


("Tim Maia",
"02:50",
"Eu Amo Você",
"https://i.scdn.co/image/ab67616d00001e02c5ba65ef4043539374a3de16",
"MPB"),

("Lil peep",
"3:00",
"Castles",
"https://i.ytimg.com/vi/As1bpICMhzs/mqdefault.jpg",
"New emo"),

("BK",
"4:00",
"te devo nada",
"https://akamai.sscdn.co/uploadfile/letras/fotos/b/e/e/e/beee81cce9563b0052fc4643d111608a.jpg",
"Trap"),

("Marisa monte",
"2:00",
"Pelo tempo que durar",
"https://i.scdn.co/image/ab67616d00001e025b7cd42c778cf9be6b2790e8",
"MPB");