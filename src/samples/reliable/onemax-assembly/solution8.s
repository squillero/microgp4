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

    movl	$-7630, %eax
    movl	$-20277, %ebx
    movl	$27647, %ecx
    movl	$6512, %edx

    xor %ebx, %eax
    jne n17
    or %ecx, %ecx
    shr $144, %ecx
    xor %edx, %ebx
    jo n17
    shl $176, %ecx
    jno n17
    shl $164, %ebx
    shr $196, %ebx
    jnc n14
n14:
    jc n18
    jnc n17
    jnz n18
n17:
    add %ebx, %ecx
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
