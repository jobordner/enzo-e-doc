#!/bin/tcsh -f

set n = 0

set prefix=heat

while ($n <= 730)
   set n0 = `printf "%03d" $n`
   echo $n0
#   convert -crop 768x768+128+128 $prefix-mesh-$n0.png mesh.png
   cp enzo-mesh-$n0.png mesh.png
#   convert -crop 768x768+128+128 $prefix-de-$n0.png   de.png
   cp enzo-temp-$n0.png   temp.png
   composite -blend 20 mesh.png temp.png $prefix-$n0.png
   @ n = $n + 1
end
