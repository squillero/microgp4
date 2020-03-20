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

    movl	$18949, %eax
    movl	$-16837, %ebx
    movl	$-32183, %ecx
    movl	$30725, %edx

    shr $243, %ebx
    and %eax, %ebx
    shr $255, %eax
    jmp n12
    shr $30, %ecx
    jnz n20
    xor %eax, %ebx
    jo n14
    jc n20
n12:
    jc n20
    cmp %ebx, %eax
n14:
    shl $183, %ebx
    shl $20, %edx
    jo n19
    jno n20
    shl $97, %ebx
n19:
    xor %ecx, %ecx
n20:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
