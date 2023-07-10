'''The flow will be like this :
 (1) Process: Compress -> Encrypt Symm
                -> Encrypt Assym
                    -> Produce Auth Params
                        -> Produce .emma
                            -> Obfuscate
                                -> Encode Base-64

 (2) Supplements: BARCODE -> Choose BARCODE Alg
                                -> Produce BARCODE
                                    ->Read BARCODE

 (3) 
'''