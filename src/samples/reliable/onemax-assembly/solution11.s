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

    movl	$4902, %eax
    movl	$-13378, %ebx
    movl	$32289, %ecx
    movl	$13059, %edx

    shl $11, %edx
    shl $4, %eax
    jmp n21
    jne n14
    xor %ecx, %ebx
    cmp %ebx, %ecx
    shr $49, %eax
    and %edx, %eax
    shl $67, %eax
    and %ecx, %edx
    shr $102, %ebx
n14:
    xor %ecx, %ecx
    sub %ecx, %edx
    and %ecx, %eax
    jo n18
n18:
    sub %ebx, %edx
    xor %ecx, %eax
    jnc n21
n21:
    jne n22
n22:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
