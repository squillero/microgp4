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

    movl	$-4595, %eax
    movl	$18727, %ebx
    movl	$5241, %ecx
    movl	$6990, %edx

    jc n11
    or %edx, %ebx
    jno n13
    cmp %ebx, %eax
    and %ecx, %eax
    shr $158, %ebx
    sub %ebx, %eax
    add %ebx, %edx
n11:
    jmp n12
n12:
    jo n16
n13:
    cmp %ebx, %edx
    shl $204, %ebx
    jnz n16
n16:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
