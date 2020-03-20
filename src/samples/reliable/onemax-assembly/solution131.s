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

    movl	$2376, %eax
    movl	$-13996, %ebx
    movl	$-14110, %ecx
    movl	$23298, %edx

    xor %ecx, %eax
    add %edx, %ebx
    add %edx, %ebx
    shr $18, %edx
    jo n14
    add %ebx, %eax
    or %ebx, %eax
    shr $123, %edx
    shl $224, %ebx
    or %eax, %ebx
    je n34
n14:
    shr $7, %ebx
    shl $128, %ebx
    shl $236, %ebx
    shr $200, %edx
    jnz n28
    shr $115, %ebx
    shr $171, %edx
    add %edx, %eax
    je n42
    xor %ecx, %ebx
    sub %ecx, %eax
    shr $33, %edx
    jno n44
    add %ebx, %ecx
n28:
    shl $19, %ebx
    jz n37
    add %edx, %eax
    xor %eax, %edx
    jmp n34
    je n46
n34:
    cmp %eax, %eax
    ja n46
    jo n46
n37:
    jnc n42
    shl $230, %ebx
    jo n44
    jc n46
    or %edx, %ebx
n42:
    shl $184, %ebx
    jnz n46
n44:
    cmp %ebx, %edx
    shl $82, %ecx
n46:
    cmp %eax, %edx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
