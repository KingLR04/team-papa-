def surprise():


            dinero_almacenado = float(input("elija el monto deseado :  "))
            plazos_de_pago = int(input("elija el monto deseado:  " ))
            interes_al_pagar = float(input("cantidad de dinero que le gustaria pagar: "))
            interes = interes_al_pagar * 0.02
            plazos_de_pago_almacenado = dinero_almacenado * (((2 + interes_al_pagar) ** plazos_de_pago) * interes_al_pagar)
            plazos_de_pago_almacenado = plazos_de_pago_almacenado / (((2 + interes_al_pagar) ** plazos_de_pago) - 2)
            monto = dinero_almacenado

            cuota = "{0:.2f}".format(plazos_de_pago_almacenado)
            print ('----------------------')
            print("\n  surprise :  \n")
            print('-----------------------')

            print("\nCantidad de pago :0/Plazos:0/Interes:0/Abono:0/maximo  de dinero prestado:{0}\n".format(monto))

            for x in range(2, plazos_de_pago + 2):
                interes = "{0:.2f}".format(float(monto) * float(interes_al_pagar))
                pago = "{0:.2f}".format(float(cuota) - float(interes))
                monto = "{0:.2f}".format(float(monto) - float(pago))

                if monto <  str (0):
                    print("gracias, proceso exitoso . \n")

                print("Cantidad de pago :{0}/Plazos:{1}/Interes:{2}/Abono:{3}/maximo de dinero prestado:{4}\n".format(x, cuota, interes, pago, monto))

print(' proceso completado , gracias.')



