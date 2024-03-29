10 REM THE ORBIT OF COMET HALLEY 
20 REM A MODEL FOR THE AMSTRAD COMPUTERS
30 REM 
40 DIM A(8,14) 
50 DIM X(14) : DIM Y(14) 
60 SYMBOL 255,24,0,24,24,24,24,24,24 
70 K =6.28 : PHD =0.59 : PH = 1986.10833 
80 SD=1985.525:TI=0.0833:N=13 
90 FOR I = 1 TO N 
100 A(6,I)= K*(SD+(I-1)*TI-PH)/(SQR(2*PHD^3))
110 IF I = 1 THEN A(1,I)=A(6,I) 
120 A(5,I)=-(A(1,I)^3+3*A(1,I)-3*A(6,I))/(3*A(1,I)^2+3) 
130 A(2,I)=A(1,I)+A(5,I) 
140 A(3,I) =A(2,I)^3+3*A(2,I)-3*A(6,I) 
150 A(4,I)=ABS (A(3,I ) 
160 IF A(4,1) <0.0001 THEN GOTO 190 
170 A(1,I)=A(2,I) 
180 GOTO 120 
190 A(7,I)=ATN( A(2, I) ) 
200 NEXT I 
210 FOR I=1 TO N 
220 A(8,I)=PHD*(1+TAN(A(7,I))^2) 
230 X(I)=40-PHD+4*A(8,I)*COS(2*A(7,I)) 
240 Y(I)=10+4*A(8,I)*SIN( 2* A(7,I)) 
250 NEXT I 
260 CLS:LOCATE 40,10: PRINT CHR$(42) 
270 FOR I= 1 TO N 
280 XX1=INT(X(I)+0.5):YY1=INT(Y(I)+1.5):LOCATE XX1,YY1 
:IF YYl<10 THEN PRINT "!" ELSE PRINT CHR$(255) 
290 XX=40+4*COS(( I-2)*PI/6):YY=10-4*(SIN((I-2)*PI/6)):LOCATE XX,YY
300 PRINT "o" 
310 FOR KK=1 TO 500:NEXT KK 
320 XX=40+4*COS(I-2)*PI/6):YY=10-4*(SIN((I-2)*PI/6)): LOCATE XX,YY
330 PRINT " " 
340 LOCATE XX1,YY1:PRINT " "
350 NEXT I 
360 GOTO 260 
