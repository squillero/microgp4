    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$31072, %eax
    movl	$-2463, %ebx
    movl	$-19775, %ecx
    movl	$-15612, %edx

    ja n14
    shr $136, %ecx
    add %ecx, %edx
    jnz n14
    ja n12
    jno n11
    jno n11
    shl $101, %ebx
n11:
    jc n18
n12:
    shr $0, %ecx
    or %eax, %eax
n14:
    shl $157, %ebx
    ja n16
n16:
    xor %eax, %eax
    cmp %edx, %eax
n18:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
