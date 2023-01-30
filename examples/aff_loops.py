from loopy.loopy_mlir import ir
from loopy.mlir import f64_t, index_t
from loopy.mlir.affine import (
    affinefor as range,
    endfor,
)
from loopy.mlir.affine_defs import d0, d1, s0, s1
from loopy.mlir.arith import constant
from loopy.mlir.func import func
from loopy.mlir.memref import aff_alloc

M = 32
N = 32
K = 32

module = ir.Module.create()

with ir.InsertionPoint(module.body):

    @func(index_t, index_t)
    def matmul(M, N):
        two = constant(1.0)
        mem = aff_alloc([10, 10], f64_t)
        for i in range(1, 10, 1):
            for j in range(1, 10, 1):
                a = (2 * d0 + 3 * d1 + 5 + s0 + 3 * s1) @ [i, j, M, N]
                v = mem[a, a]
                w = v * two
                mem[a, a] = w
            endfor()
        endfor()


module.operation.print()