#! /usr/bin/env python
#
def subtriangle_next ( n, more, i1, j1, i2, j2, i3, j3 ):

#*****************************************************************************80
#
## SUBTRIANGLE_NEXT computes the next subtriangle of a triangle.
#
#  Discussion:
#
#    The three sides of a triangle have been subdivided into N segments,
#    inducing a natural subdivision of the triangle into N*N subtriangles.
#    It is desired to consider each subtriangle, one at a time, in some
#    definite order.  This routine can produce information defining each 
#    of the subtriangles, one after another.
#
#    The subtriangles are described in terms of the integer coordinates 
#    (I,J) of their vertices.  These coordinates both range from 0 to N,
#    with the additional restriction that I + J <= N.
#
#    The vertices of each triangle are listed in counterclockwise order.
#
#  Example:
#
#    N = 4
#
#    4  *
#       |\
#       16\
#    3  *--*
#       |14|\
#       13\15\
#    2  *--*--*
#       |\9|11|\
#       |8\10\12\
#    1  *--*--*--*
#       |\2|\4|\6|\
#       |1\|3\|5\|7\
#   0   *--*--*--*--*
#
#       0  1  2  3  4
#
#    Rank  I1 J1  I2 J2  I3 J3
#    ----  -----  -----  ----- 
#       1   0  0   1  0   0  1
#       2   1  1   0  1   1  0
#       3   1  0   2  0   1  1
#       4   2  1   1  1   2  0
#       5   2  0   3  0   2  1
#       6   3  1   1  1   3  0
#       7   3  0   4  0   3  1
#       8   0  1   1  1   0  2
#       9   1  2   0  2   1  1
#      10   1  1   2  1   1  2
#      11   2  2   1  2   2  1
#      12   2  1   3  1   2  2
#      13   0  2   1  2   0  3
#      14   1  3   0  3   1  2
#      15   1  2   2  2   1  3
#      16   0  3   1  3   0  4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, indicates the number of subdivisions of each side
#    of the original triangle.
#
#    Input, logical MORE.  On first call, set MORE to FALSE.  Thereafter, 
#    the input value of MORE should be the output value from the previous
#    call.
#
#    Input, integer I1, J1, I2, J2, I3, J3, the indices of the vertices 
#    of the subtriangle as computed on the previous call.  On the first call
#    with MORE set to FALSE, set these values to 0.
#
#    Output, logical MORE, the output value of MORE will be TRUE if there 
#    are more subtriangles that can be generated by further calls.  However, 
#    if MORE is returned as FALSE, the accompanying subtriangle information 
#    refers to the last subtriangle that can be generated.
#
#    Output, integer I1, J1, I2, J2, I3, J3, the indices of the 
#    vertices of the subtriangle.
#
  if ( n < 1 ):
    more = False
    return more, i1, j1, i2, j2, i3, j3

  if ( not more ):

    i1 = 0
    j1 = 0
    i2 = 1
    j2 = 0
    i3 = 0
    j3 = 1

    if ( n == 1 ):
      more = False
    else:
      more = True
#
#  We last generated a triangle like:
#
#    2---1
#     \  |
#      \ |
#       \|
#        3
#
  elif ( i2 < i3 ):

    i1 = i3
    j1 = j3
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1
#
#  We last generated a triangle like
#
#    3
#    |\
#    | \
#    |  \
#    1---2
#
  elif ( i1 + 1 + j1 + 1 <= n ):

    i1 = i1 + 1
    j1 = j1 + 1
    i2 = i1 - 1
    j2 = j1
    i3 = i1
    j3 = j1 - 1
#
#  We must be at the end of a row.
#
  else:

    i1 = 0
    j1 = j1 + 1
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1

    if ( n <= j1 + 1 ):
      more = False

  return more, i1, j1, i2, j2, i3, j3

def subtriangle_next_test ( ):

#*****************************************************************************80
#
## SUBTRIANGLE_NEXT_TEST tests SUBTRIANGLE_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4
  rank = 0

  more = False
  i1 = 0
  j1 = 0
  i2 = 0
  j2 = 0
  i3 = 0
  j3 = 0

  print ''
  print 'SUBTRIANGLE_NEXT_TEST'
  print '  SUBTRIANGLE_NEXT generates the indices of subtriangles'
  print '  in a triangle whose edges were divided into N subedges.'
  print ''
  print '  For this test, N = %d' % ( n  )
  print ''
  print '  Rank    I1  J1    I2  J2    I3  J3'
  print ''

  while ( True ):

    more, i1, j1, i2, j2, i3, j3 = subtriangle_next ( n, more, \
      i1, j1, i2, j2, i3, j3 )

    rank = rank + 1

    print '  %4d    %2d  %2d    %2d  %2d    %2d  %2d' \
      % ( rank, i1, j1, i2, j2, i3, j3 )

    if ( not more ):
      break
#
#  Terminate.
#
  print ''
  print 'SUBTRIANGLE_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subtriangle_next_test ( )
  timestamp ( )

