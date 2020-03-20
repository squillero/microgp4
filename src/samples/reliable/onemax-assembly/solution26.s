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

    movl	$10152, %eax
    movl	$-26279, %ebx
    movl	$21868, %ecx
    movl	$-699, %edx

    xor %edx, %ecx
    ja n27
    shr $227, %edx
    shr $233, %edx
    shr $196, %edx
    shl $124, %ebx
    cmp %eax, %eax
    or %ebx, %ebx
    cmp %edx, %eax
    xor %ebx, %eax
    shl $68, %edx
    jno n27
    shl $226, %edx
    xor %edx, %ebx
    shl $230, %ecx
    je n27
    shl $122, %ecx
    jo n22
    cmp %ecx, %ebx
n22:
    shl $171, %ecx
    shr $70, %ebx
    shr $196, %ebx
    shr $32, %edx
    or %ecx, %edx
n27:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
