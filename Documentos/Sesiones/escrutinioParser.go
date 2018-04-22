package main

import (
	"os"
	"fmt"
	"log"
    "github.com/tealeg/xlsx"
)

func main() {

	for i := 1; i < 9; i++ {
		excelFileName := fmt.Sprintf("./actas2/ActaSesion%d.xlsx",i)
		xlFile, err := xlsx.OpenFile(excelFileName)
		if err != nil {
			log.Println(err)
			os.Exit(1)
		}
		parseAct(xlFile)
	}
}

func parseAct(file *xlsx.File){
    for _, sheet := range file.Sheets {
		for i := 1; i < len(sheet.Rows[2].Cells); i++ {
			junta,_:= sheet.Rows[2].Cells[i].Int()
			pac,_:= sheet.Rows[3].Cells[i].Int()
			rn,_:= sheet.Rows[4].Cells[i].Int()
			nulos,_:= sheet.Rows[6].Cells[i].Int()
			blancos,_:= sheet.Rows[7].Cells[i].Int()
			votos,_:= sheet.Rows[8].Cells[i].Int()
			fmt.Printf("%d,",junta)
			fmt.Printf("%d,",pac)
			fmt.Printf("%d,",rn)
			fmt.Printf("%d,",nulos)
			fmt.Printf("%d,",blancos)
			fmt.Printf("%d",votos)
			// for j := 2; j < 11; j++ {
			// 	if j==2 || j==19{
			// 	k,_:= sheet.Rows[j].Cells[i].Int()
			// 	if j == 2 {
			// 		fmt.Printf("%d,",k)
			// 	}else{
			// 		fmt.Printf("%d",k)
			// 	}}
			// }
			fmt.Printf("\n")
		}
	}
}
