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

    movl	$25793, %eax
    movl	$18935, %ebx
    movl	$12805, %ecx
    movl	$6843, %edx

    jnc n43
    shr $232, %edx
    xor %edx, %edx
    shl $115, %ebx
    or %eax, %edx
    cmp %ebx, %ecx
    shl $187, %eax
    ja n47
    jo n35
    shr $246, %eax
    jnz n47
    shl $238, %eax
    jno n21
    shr $241, %eax
    shl $27, %ecx
    shr $240, %edx
    shl $169, %edx
    jc n46
n21:
    and %ecx, %ebx
    ja n45
    xor %ecx, %ecx
    shr $242, %ebx
    xor %eax, %ecx
    cmp %eax, %ecx
    jo n30
    shr $39, %ecx
    shl $67, %ecx
n30:
    shl $131, %eax
    cmp %eax, %ebx
    shr $228, %ecx
    jnz n42
    cmp %ebx, %edx
n35:
    sub %eax, %ecx
    add %ebx, %ebx
    or %edx, %edx
    je n49
    or %ebx, %ebx
    xor %ecx, %eax
    jne n43
n42:
    shr $85, %edx
n43:
    jnc n47
    shl $243, %ebx
n45:
    or %edx, %edx
n46:
    and %ebx, %edx
n47:
    add %ecx, %edx
    jnc n49
n49:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
