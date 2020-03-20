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

    movl	$1089, %eax
    movl	$29364, %ebx
    movl	$-20247, %ecx
    movl	$-27158, %edx

    shr $233, %edx
    shr $196, %edx
    shl $124, %ebx
    cmp %eax, %eax
    or %ebx, %ebx
    cmp %edx, %eax
    xor %ebx, %eax
    shl $68, %edx
    jno n30
    shl $226, %edx
    or %ecx, %edx
    xor %edx, %ebx
    shl $230, %ecx
    je n25
    shl $122, %ecx
    jo n20
    cmp %ecx, %ebx
n20:
    shl $171, %ecx
    shr $70, %ebx
    shr $196, %ebx
    shr $32, %edx
    or %ecx, %edx
n25:
    jnc n26
n26:
    je n30
    shl $10, %edx
    or %eax, %ecx
    jne n31
n30:
    jnc n31
n31:
    jo n32
n32:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
