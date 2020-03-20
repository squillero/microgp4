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

    movl	$30872, %eax
    movl	$3488, %ebx
    movl	$23644, %ecx
    movl	$28995, %edx

    jnz n7
    jnc n44
    or %ecx, %ebx
    jz n30
n7:
    shr $60, %eax
    cmp %edx, %edx
    cmp %edx, %eax
    shr $104, %ebx
    jne n30
    jo n37
    jnz n41
    je n34
    shr $144, %ebx
    shl $92, %edx
    shr $14, %ecx
    jne n26
    shl $127, %ecx
    shl $43, %eax
    or %ebx, %ecx
    cmp %edx, %ebx
    cmp %edx, %edx
    cmp %ecx, %eax
    shr $30, %eax
n26:
    jc n34
    or %ecx, %eax
    ja n37
    shl $154, %edx
n30:
    shl $67, %eax
    xor %ebx, %ecx
    sub %edx, %ecx
    jo n36
n34:
    jz n40
    cmp %edx, %ebx
n36:
    and %eax, %ecx
n37:
    ja n40
    or %ecx, %ecx
    or %ecx, %ecx
n40:
    shl $160, %edx
n41:
    jnz n44
    jo n43
n43:
    jno n45
n44:
    shr $96, %ebx
n45:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
