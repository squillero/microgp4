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

    movl	$17627, %eax
    movl	$-23893, %ebx
    movl	$17421, %ecx
    movl	$9274, %edx

    jnc n27
    shl $229, %edx
    jnc n8
    shr $178, %eax
    sub %edx, %ebx
n8:
    je n35
    ja n34
    add %ecx, %edx
    shl $194, %ebx
    sub %edx, %ecx
    jnz n22
    sub %eax, %eax
    jnc n35
    add %ebx, %ebx
    shr $51, %eax
    jo n20
    je n21
n20:
    shl $224, %ebx
n21:
    xor %ebx, %eax
n22:
    shr $148, %ebx
    cmp %ecx, %ecx
    shr $154, %ebx
    shr $211, %ecx
    jne n27
n27:
    jno n30
    cmp %edx, %edx
    shr $176, %edx
n30:
    xor %ecx, %edx
    shl $76, %ecx
    shl $94, %edx
    je n34
n34:
    shl $73, %edx
n35:
    ja n36
n36:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
