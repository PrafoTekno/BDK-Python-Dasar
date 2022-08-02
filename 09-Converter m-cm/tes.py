
print ("\nConverter satuan panjang\n")

input_meter = float (input ("Masukan nilai besar dalam m : "))
hasil_cm = input_meter * 100
hasil_dm = input_meter * 10
hasil_mm = input_meter * 1000
hasil_hm = input_meter * 0.01
hasil_km = input_meter * 0.001
hasil_dam = input_meter * 0.1

print ("\n")

print (input_meter, " m = ", hasil_km, " km")
print (input_meter, " m = ", hasil_hm, " hm")
print (input_meter, " m = ", hasil_dam, " dam")
print (input_meter, " m = ", hasil_dm, " dm")
print (input_meter, " m = ", hasil_cm, " cm")
print (input_meter, " m = ", hasil_mm, " mm")

print ("\n")